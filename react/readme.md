```jsx
// 父组件
class ParentComponent extends React.Component {
  //创建一个handleDataFromChild 给子调用
  handleDataFromChild = (dataFromChild) => {
    console.log("Data received from child:", dataFromChild);
    // 在这里可以进一步处理从子组件传递过来的数据
  };

  render() {
    return (
      <div>
        //   ParentComponen 把this.handleDataFromChild 创建成onDataFromChild给子调用，
        <ChildComponent onDataFromChild={this.handleDataFromChild} />
      </div>
    );
  }
}


class ChildComponent extends React.Component {
  sendDataToParent = () => {
    const data = "Data from child";
    // 调用父组件传递过来的回调函数onDataFromChild
    this.props.onDataFromChild(data);
  };

  render() {
    return (
      <div>
        <button onClick={this.sendDataToParent}>Send Data to Parent</button>
      </div>
    );
  }
}
```

```jsx
import React, { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  componentDidMount() {
    // 在组件挂载后订阅事件
    document.addEventListener('click', this.handleDocumentClick);
  }

  componentDidUpdate(prevProps, prevState) {
    // 在组件更新后检查计数值是否超过某个阈值
    if (this.state.count > 10 && this.state.count !== prevState.count) {
      alert('Count is greater than 10!');
    }
  }

  componentWillUnmount() {
    // 在组件卸载前取消订阅事件
    document.removeEventListener('click', this.handleDocumentClick);
  }

  handleDocumentClick = () => {
    // 处理文档点击事件
    this.setState(prevState => ({
      count: prevState.count + 1
    }));
  };

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.handleDocumentClick}>Increment</button>
      </div>
    );
  }
}

export default Counter;

```