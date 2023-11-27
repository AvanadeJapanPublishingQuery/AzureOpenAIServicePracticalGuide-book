import json
# training set をロードする
with open('training_set.jsonl', 'r', encoding='utf-8') as f:
 training_dataset = [json.loads(line) for line in f]
# トレーニング用データの内容を表示する
print("Number of examples in training set:", len(training_dataset))
print("First example in training set:")
for message in training_dataset[0]["messages"]:
 print(message)
# validation set をロードする
with open('validation_set.jsonl', 'r', encoding='utf-8') as f:
 validation_dataset = [json.loads(line) for line in f]
# バリデーション用データの内容を表示する
print("\nNumber of examples in validation set:", len(validation_dataset))
print("First example in validation set:")
for message in validation_dataset[0]["messages"]:
 print(message)