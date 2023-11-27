import os
import openai
import requests
import json

# Azure OpenAIのAPIキー
openai.api_key = "OPENAI_API_KEY"
# "2023-07-01-preview" 以降のバージョンを指定
openai.api_version = "2023-07-01-preview"
# "azure"を指定
openai.api_type = "OPENAI_API_TYPE"
# AzureOpenAIのエンドポイント （例："https://myinstance01.openai.azure.com/"）
openai.api_base = "OPENAI_API_BASE"
# Azure OpenAIのデプロイ名
openai_deployment = "OPENAI_DEPLOYMENT"
# Bing SearchのAPIキー
bing_api_key = "BING_API_KEY"
# Bing Searchのリソースのエンドポイントを指定
bing_base_url = "BING_BASE_URL"


def get_bing_search(query: str) -> list:
    # Bing Search APIのエンドポイントを設定
    endpoint = bing_base_url + "v7.0/search/"
    # リクエストヘッダーにAPIキーを設定
    headers = {"Ocp-Apim-Subscription-Key": bing_api_key}
    # リクエストパラメータを設定
    params = {
        "q": query,     # 検索キーワード
        "mkt": 'ja-JP',  # 検索市場を日本に指定
        "count": 3,     # 検索結果数
        "safeSearch": 'Strict',     # セーフサーチ
        "responseFilter": 'Webpages'  # カテゴリをWebページに絞る
    }

    try:
        # APIリクエストを実行し、レスポンスを取得
        response = requests.get(endpoint, headers=headers, params=params)
        # レスポンスステータスのチェック
        response.raise_for_status()
        # 検索結果を抽出
        search_results = response.json()["webPages"]["value"]

        web_responses = []
        for result in search_results:
            # 各検索結果をディクショナリに格納
            web_response = {
                "name": result["name"],         # 検索結果のタイトル
                "url": result["url"],           # 検索結果のURL
                "snippet": result["snippet"]    # 検索結果の短い説明
            }
            web_responses.append(web_response)

        # 検索結果のリストを返却
        return web_responses
    # エラー処理
    except requests.RequestException as e:
        print(f'Request failed: {e}')
    except KeyError as e:
        print(f'Key Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    return None


def make_completion(messages: list, functions: list):
    # モデルにリクエストを送信
    response = openai.ChatCompletion.create(
        engine=openai_deployment,      # Azure OpenAIのデプロイ名を指定
        messages=messages,             # ユーザーとアシスタントの会話履歴
        functions=functions,           # 呼び出し可能な関数のリスト
        function_call="auto",          # 関数呼び出しを自動に設定
        max_tokens=1000,               # トークンの最大数
        temperature=0                  # モデルの出力の多様性を制御する
    )
    response_message = response["choices"][0]["message"]

    # 途中経過を出力
    print()
    print("######################################")
    print("2. モデルが関数を呼び出すと判断した場合、関数の引数を生成する")
    print("######################################")
    print(json.dumps(response_message, indent=2, ensure_ascii=False))

    if response.choices[0].finish_reason == 'function_call':
        # モデルが関数呼び出しを決定した場合
        function_name = response_message["function_call"]["name"]
        # 利用可能な関数のリストを定義
        available_functions = {
            "get_bing_search": get_bing_search,
        }
        # 呼び出す関数を選択
        function_to_call = available_functions[function_name]
        # 関数の引数を解析
        function_args = json.loads(
            response_message["function_call"]["arguments"])
        function_response = function_to_call(**function_args)

        # 途中経過を出力
        print()
        print("######################################")
        print("3. 関数を実行し、APIから結果を取得")
        print("######################################")
        for res in function_response:
            print(f"Name: {res['name']}")
            print(f"URL: {res['url']}")
            print(f"Snippet: {res['snippet']}")

        # 関数の実行結果をJSON形式で整形
        formatted_function_response = json.dumps(
            function_response, indent=2, ensure_ascii=False)

        # 関数の実行結果をメッセージに追加
        messages.append({"role": "assistant", "content": formatted_function_response})

        # 途中経過を出力
        print()
        print("######################################")
        print("4. 質問と関数の実行結果をモデルに再送信して要約を依頼")
        print("######################################")
        print(json.dumps(messages, indent=2, ensure_ascii=False))

        # モデルに再度リクエストを送信して最終的な回答を生成
        second_response = openai.ChatCompletion.create(
            engine=openai_deployment,
            messages=messages,
            max_tokens=1000,
            temperature=0
        )
        return second_response.choices[0].message.content
    else:
        # 関数呼び出しがない場合は元のメッセージを返却
        return response.choices[0].message.content


def handle_message(event):
    messages = [
        # システムメッセージ
        {"role": "system", "content": "あなたはBing Searchで最新情報を検索し、検索結果を要約し簡潔な言葉で回答するアシスタントです。"},
        # ユーザーからの入力
        {"role": "user", "content": event},
    ]
    # 呼び出し可能な関数の定義
    functions = [
        {
            "name": "get_bing_search",  # 関数名
            "description": "Bing Searchで最新情報を検索する",  # 関数の説明
            "parameters": {  # 関数のパラメーターを定義
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Bing Searchの検索キーワード"  # パラメーターの説明
                    }
                },
                "required": ["query"]}  # 必須パラメーター
        }
    ]
    # 途中経過を出力
    print()
    print("######################################")
    print("1. 質問と関数の定義をモデルに送信")
    print("######################################")
    print(json.dumps(messages, indent=2, ensure_ascii=False))
    print(json.dumps(functions, indent=2, ensure_ascii=False))

    # モデルにメッセージと関数を送信し、回答を生成
    return make_completion(messages, functions)


def main():
    # ユーザーからの質問を受け付ける
    user_input = input("質問を入力してください: ")
    # 入力された質問を処理し、回答を生成する
    response = handle_message(user_input)

    print()
    print("######################################")
    print("5. 最終的な回答を生成")
    print("######################################")
    # 生成された回答を出力
    print(response)


main()  # メイン処理を実行する
