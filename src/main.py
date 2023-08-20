from load_data import load_data
from eda import eda
from feat_eng import feature_eng
from train import train_model
from model_exp import model_exp
def main():
    
    filepath = '/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/data/raw/merged_data.csv'

    # Load data
    X_train, X_test, y_train, y_test = load_data(filepath)

    X_train,y_train, X_test, y_test = eda(X_train, y_train, X_test, y_test)

    X_train, X_test, y_train, y_test = feature_eng(X_train, X_test, y_train, y_test)

    train_model (X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()


