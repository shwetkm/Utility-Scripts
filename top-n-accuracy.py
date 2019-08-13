def top_n_accuracy(preds, truths, n):
    """
    both preds and truths are same shape m by n (m is number of predictions and n is number of classes)
    """
    best_n = np.argsort(preds, axis=1)[:,-n:]
    ts = np.argmax(np.array(truths),axis=1)
    successes = 0
    for i in range(ts.shape[0]):
        if ts[i] in best_n[i,:]:
            successes += 1
    return float(successes)/ts.shape[0]
    
if __name__ == '__main__':
  prob_pred = logreg.predict_proba(X_val)
  y_val_dummy = pd.get_dummies(y_val).reset_index(drop=True)
  y_val_dummy.columns = range(0,38)
  top_n_accuracy(prob_pred,y_val_dummy,3)
