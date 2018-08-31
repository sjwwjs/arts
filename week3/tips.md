## 为什么逻辑回归要用sigmoid 函数
- 为了解答你的疑惑，需要从Logistic Regression（下面简称LR）的推到说起，为了方便起见，我们只讨论二分类的情况。
首先，LR的假设只有一个，就是两个类别的特征服从均值不等，方差相等的高斯分布，也就是
- p(x|y=0)∼N(μ0,σ)

- p(x|y=1)∼N(μ1,σ)


- 为什么会假设它们服从高斯分布？一方面是因为高斯分布是比较容易处理的分布，另一方面，从信息论的角度上看，当均值和方差已知时（尽管你并不知道确切的均值和方差，但是根据概率论，当样本量足够大时，样本均值和方差以概率1趋向于均值和方差），高斯分布是熵最大的分布，为什么要熵最大？因为最大熵的分布可以平摊你的风险，这就好比不要把鸡蛋放到同一个篮子里，想想二分查找中，为什么每次都是选取中间点作为查找点？就是为了平摊风险。为什么假设方差相等？为了后面处理起来方便....不相等的话没法消去。。。
- 接下来就是贝叶斯决策的东西了，首先，我们定义风险
- R(y=0|x)=λ00P(y=0|x)+λ01P(y=1|x)

- R(y=1|x)=λ10P(y=0|x)+λ11P(y=1|x)
- 其中，R(y=0|x)是把样本预测为0时的风险，R(y=1|x)是把样本预测为1时的风险，λij是样本实际标签为j时，却把它预测为i是所带来的风险。



- 在LR里，我们认为预测正确并不会带来风险，因此λ00和λ11都为0，此外，我们认为当标签为0而预测为1 和 当标签为1而预测为0，这两者所带来的风险是相等的，因此λ10和λ01相等，方便起见，我们记为λ。这里你可能认为我说的是废话，但在一些领域里，比如医学、风控等，这些λ在大多数情况下是不相等的，有时候我们会选择“宁可杀错一百也不能放过一个”
所以，上面定义的风险就可以简化为

- R(y=0|x)=λP(y=1|x)

- R(y=1|x)=λP(y=0|x)



- 现在问题来了，我拿到一个样本，我应该把它预测为0还是预测为1好？按照风险最小化的原则，我们应该选择风险最小的，也就是，当
- R(y=0|x)<R(y=1|x)
- 时，预测为0的风险要小于预测为1的风险，即
- P(y=1|x)<P(y=0|x)


- 时，应该把样本预测为0，从而也就是书上提到的：比较两个条件概率，并把样本分配到概率最大的那个类上我们两边除一下，就会得到
- P(y=1|x)/P(y=0|x)<1

- 我们对不等式左边的部分取一下对数，（为什么取对数？因为之前我们提过，两个类别的特征服从均值不等，方差相等的高斯分布，取对数方便处理高斯分布里的指数），再利用贝叶斯公式进行展开，归一化常数扔掉，我们将得到
- 两面取指数，并且利用上P(y=1|x)+P(y=0|x)=1这个概率公理，移一下，你就会看到熟悉的logistic公式
- 综上，你的第一个问题解答了，Logistic函数并不是假设出来的，而是推导出来的
第二个问题，我们在贝叶斯决策那里解释了
第三个问题，由于logistic函数并不是假设出来的，你说的命题并不成立，并不是为了归一化而提出logistic函数，而是logistic函数恰好具备归一化特性，至于为什么是线性，你看倒数第二个公式就明白了，取了对数后，就是线性的
