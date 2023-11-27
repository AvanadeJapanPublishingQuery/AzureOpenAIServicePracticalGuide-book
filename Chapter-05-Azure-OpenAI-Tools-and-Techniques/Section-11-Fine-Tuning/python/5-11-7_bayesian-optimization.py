from sklearn.datasets import load_iris
from scipy.stats import uniform, randint
class ChatGPTModel:
    def __init__(self, epochs, batch_size, lr_multiplier, prompt_loss_weight):
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr_multiplier = lr_multiplier
        self.prompt_loss_weight = prompt_loss_weight
    
    def fit(self, data, target):
        pass # 今回はダミーのトレーニング処理
    def evaluate(self, data, target):
        return uniform.rvs() # ダミーの評価処理

if __name__ == '__main__':
     # 仮のデータセット
    iris = load_iris()
    data = iris.data
    target = iris.target
    num_trials = 10
    best_score = float('-inf')
    best_params = None
    for _ in range(num_trials):
        epochs = randint.rvs(1, 10)
        batch_size = randint.rvs(32, 256)
        lr_multiplier = uniform.rvs(0.001, 0.1)
        prompt_loss_weight = uniform.rvs(0, 1)
        model = ChatGPTModel(epochs, batch_size, lr_multiplier, prompt_loss_weight)
        model.fit(data, target)
        score = model.evaluate(data, target)
        
        if score > best_score:
            best_score = score
            best_params = {
                'epochs': epochs,
                'batch_size': batch_size,
                'lr_multiplier': lr_multiplier,
                'prompt_loss_weight': prompt_loss_weight
            }
        print(f"Parameters: {best_params}, Score: {score}")
    print(f"Best Parameters: {best_params}, Best Score: {best_score}")