from scipy.stats import uniform
from sklearn.datasets import load_iris

class ChatGPTModel:
    def __init__(self, epochs, batch_size, lr_multiplier, prompt_loss_weight):
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr_multiplier = lr_multiplier
        self.prompt_loss_weight = prompt_loss_weight

    def fit(self, data, target):
        return uniform.rvs()
 
    def evaluate(self, data, target):
        return uniform.rvs()

if __name__ == '__main__': # Irisデータセットをロード
    iris = load_iris()
    data, target = iris.data, iris.target
    # 探索したいハイパーパラメータの値のリストを定義
    epochs_values = [1, 5, 10]
    batch_size_values = [32, 64, 128, 256]
    lr_multiplier_values = [0.001, 0.01, 0.1]
    prompt_loss_weight_values = [0, 0.5, 1]
    # ベストスコアの追跡のための変数を初期化
    best_score = float('-inf')
    best_params = None
    for epochs in epochs_values: # すべての組み合わせを試す
        for batch_size in batch_size_values:
            for lr_multiplier in lr_multiplier_values:
                for prompt_loss_weight in prompt_loss_weight_values:
                    model = ChatGPTModel(epochs, batch_size, lr_multiplier, prompt_loss_weight)
                    score = model.evaluate(data, target)

                    # スコアがベストスコアより良ければ、更新する
                    if score > best_score:
                        best_score = score
                        best_params = {
                            'epochs': epochs,
                            'batch_size': batch_size,
                            'lr_multiplier': lr_multiplier,
                            'prompt_loss_weight': prompt_loss_weight
                        }
                    # 結果の表示
                    params = {
                        'epochs': epochs,
                        'batch_size': batch_size,
                        'lr_multiplier': lr_multiplier,
                        'prompt_loss_weight': prompt_loss_weight
                    }
                    print(f"Parameters: {params}, Score: {score}")
    # ベストスコアとその時のパラメータを出力
    print(f"\nBest Score: {best_score}")
    print(f"Best Parameters: {best_params}")