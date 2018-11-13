from sklearn.metrics import roc_curve, auc
 
def plot_auc_roc(expected_labels,our_labels):
  ### actual code for roc + threshold charts start here 
  # compute fpr, tpr, thresholds and roc_auc
  fpr, tpr, thresholds = roc_curve(expected_labels, our_labels)
  roc_auc = auc(fpr, tpr) # compute area under the curve
  # print(thresholds)
  plt.figure()
  plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % (roc_auc))
  plt.plot([0, 1], [0, 1], 'k--')
  plt.xlim([0.0, 1.0])
  plt.ylim([0.0, 1.05])
  plt.xlabel('False Positive Rate')
  plt.ylabel('True Positive Rate')
  plt.title('Receiver operating characteristic')
  plt.legend(loc="lower right")

  # create the axis of thresholds (scores)
  ax2 = plt.gca().twinx()
  ax2.plot(fpr, thresholds, markeredgecolor='r',linestyle='dashed', color='r')
  ax2.set_ylabel('Threshold',color='r')
  ax2.set_ylim([thresholds[-1],thresholds[0]])
  ax2.set_xlim([fpr[0],fpr[-1]])

  plt.show()
