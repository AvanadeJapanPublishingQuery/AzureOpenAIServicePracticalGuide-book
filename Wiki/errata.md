# 書籍：「Azure OpenAI Service実践ガイド ～ LLMを組み込んだシステム構築」の正誤表

下記の誤りがありました。お詫びして訂正いたします。

本ページに掲載されていない誤植など間違いを見つけた方は、[issue](https://github.com/AvanadeJapanPublishingQuery/AzureOpenAIServicePracticalGuide-book/issues)  までお知らせください。

# 第2刷まで
| 頁 | 誤 | 正 |
| ---- | ---- | ---- |
| 5.7 P.253 コード 5.7.4 L.2 | (記載が抜けていた) | using Microsoft.SemanticKernel.Planning; |
| 5.7 P.255 L.4 | https://github.com/microsoft/semantic-kernel/tree/main/samples/skills | https://github.com/microsoft/semantic-kernel/tree/python-0.3.15.dev/samples/skills |
| 5.7 P.255 コード5.7.5 L.25 | plugin_directory = "../../samples/plugin/" | plugin_directory = "../../samples/skills/" |

### 5.7 P.253 
　コード 5.7.4 OpenAI規格プラグインの実行 (C#)  
　のサンプルコードの記述において  
　using Microsoft.SemanticKernel.Planning;  
　の記述が抜けておりました。  

　リポジトリのサンプルコードは問題ございません。  
　リポジトリの修正はございません。  
　[Program.cs](https://github.com/AvanadeJapanPublishingQuery/AzureOpenAIServicePracticalGuide-book/blob/main/Chapter-05-Azure-OpenAI-Tools-and-Techniques/Section-07-Semantic-Kernel/CSharp/cs_plugin_demo/Program.cs)  

### 5.7 P.255 
　詳細は、issue #4 に記載致しました。  
　https://github.com/AvanadeJapanPublishingQuery/AzureOpenAIServicePracticalGuide-book/issues/4  

