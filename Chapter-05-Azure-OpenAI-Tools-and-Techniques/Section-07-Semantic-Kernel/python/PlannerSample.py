import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.core_skills.text_skill import TextSkill
from semantic_kernel.planning.basic_planner import BasicPlanner

# Azure OpenAI API Keyの設定
api_key = "YOUR AZURE OPENAI API KEY"
endpoint = "YOUR AZURE OPENAI ENDPOINT"
deployment = "gpt-35-turbo-16k"

kernel = sk.Kernel()
kernel.add_chat_service("chat_completion", AzureChatCompletion(deployment, endpoint, api_key))

#plannerに依頼する内容を設定
ask = """
明日はクリスマスだ。デートのアイデアをいくつか考えないと。
彼女は英語を話すので、英語で書きましょう。
テキストを大文字に変換しなさい。
"""

#必要なpluginをインポート
#https://github.com/microsoft/semantic-kernel/tree/main/samples/pluginsからダウンロードしてローカルでインポート
plugin_directory = "../../samples/plugin/"
summarize_plugin = kernel.import_semantic_plugin_from_directory(plugin_directory, "SummarizePlugin")
writer_plugin = kernel.import_semantic_plugin_from_directory(plugin_directory, "WriterPlugin")
text_plugin = kernel.import_plugin(TextSkill(), "TextPlugin")

#BasicPlannerを使って、必要なpluginを抽出、処理順を設定
planner = BasicPlanner()
basic_plan = await planner.create_plan_async(ask, kernel)

#設定したplanを確認
print(basic_plan.generated_plan)

results = await planner.execute_plan_async(basic_plan, kernel)
print(results)