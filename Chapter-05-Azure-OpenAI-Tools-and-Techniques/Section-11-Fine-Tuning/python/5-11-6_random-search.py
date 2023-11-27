from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.stats import uniform

# 仮のChatGPTModelの定義（ダミーのモデルとして）
class ChatGPTModel:
    def fit(self, data, target): # モデルのトレーニングロジック
        return self
    def score(self, data, target): # モデルの評価ロジック
        return uniform.rvs() # 今回はランダムなスコアを返すようにします
    def get_params(self, deep=True): # ハイパーパラメータの取得
        return {}
    def set_params(self, **params): # ハイパーパラメータの設定
        for key, value in params.items(): 
            setattr(self, key, value)
        return self
    
# データの準備
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=42)
def objective(params): # ハイパーパラメータ探索の目的関数
    model = ChatGPTModel()
    model.set_params(**params)
    model.fit(X_train, y_train)
    return {'loss': -model.score(X_test, y_test), 'status': STATUS_OK}

# ハイパーパラメータ探索の範囲を定義
space = {
    'epochs': hp.randint('epochs', 10) + 1,
    'batch_size': hp.choice('batch_size', [32, 64, 128, 256]),
    'lr_multiplier': hp.loguniform('lr_multiplier', -4, -1),
    'prompt_loss_weight': hp.uniform('prompt_loss_weight', 0, 1)
}

# 実行
trials = Trials()
best = fmin(fn=objective, space=space, algo=tpe.suggest, max_evals=32, trials=trials)
# 最適なパラメータの表示
print("Best parameters found: ", best)