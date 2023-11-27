import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

# Azure OpenAI API Keyの設定
api_key = "YOUR AZURE OPENAI API KEY"
endpoint = "YOUR AZURE OPENAI ENDPOINT"
deployment = "gpt-35-turbo-16k"

kernel = sk.Kernel()
# Configure AI service used by the kernel
kernel.add_text_completion_service("dv", AzureChatCompletion(deployment, 
endpoint, api_key))
prompt = """{{$input}}
上記の内容を要約して.
"""
summarize = kernel.create_semantic_function(prompt, max_tokens=2000, 
temperature=0.2, top_p=0.5)

input_text = """
GPT-4（ジーピーティーフォー、Generative Pre-trained Transformer 4）とは、OpenAIによって開発されたマルチモーダル（英語版）大規模言語モデルである[1]。
2023年3月14日に公開された[2]。自然言語処理にTransformerを採用しており、教師なし学習によって大規模なニューラルネットワークを学習させ、その後、人間のフィードバックからの強化学習（RLHF）を行っている[3]。
マイクロソフトは公表前から本言語モデルをBingに搭載していた[4]。

OpenAIはGPT-4を発表した記事において、「GPT-4はGPT-3.5よりも遥かに創造的で信頼性が高く、より細かい指示に対応できる」と紹介している[2]。
GPT-4は25000語以上のテキストを同時に読み取ることができ、これは以前のバージョンに比べると大幅に改良されている[5][6]。
GPT-4は「安全性のリスク」と「競争上のリスク」を考慮し、あえてパラメータを明示するのを控えている。
技術報告書内では人間とAIのデータを用いて強化学習を行ったという事実以外は、モデルサイズ、ハードウェア、アーキテクチャ、トレーニング方法、訓練データ、人間のフィードバックからの強化学習に何人月を投じたかなどの開示はしていない[3]。
そのため、GPT-4の正確なパラメータ数は不明である。
ザ・ヴァージはGPT-3は1750億個のパラメータを持つのに対してGPT-4は100兆個のパラメータを持つと報じていたが、
前述の理由でOpenAIのCEOであるサム・アルトマンはこれを「まったくのでたらめだ」と否定している[7]
"""

#先程設定したinput_textを要約する
summary = summarize(input_text)

print(summary)