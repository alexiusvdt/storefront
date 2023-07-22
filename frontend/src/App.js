import logo from './logo.svg';
import './App.css';
import React, { Component } from "react";

const stuffToPassIn = [
  {
    id: 1,
    title: "Go to Market",
    description: "Buy ingredients to prepare dinner",
    completed: true,
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stateObject: {},
      stateThing: []
      // stateful items go here
      // probably shopping cart / sesh / last viewed pages
    };
  }

  async componentDidMount() {
    try {
      const endpoint = "products"
      const res = await fetch(`http://localhost:8000/api/${endpoint}/`);
      const stateThing = await res.json();
      this.setState({
        stateThing: [...stateThing]
      });
      console.log(stateThing)
    } catch (e) {
      console.log(e);
    }
  }

  // this is old code from a todo app just as a placeholder
  // renderItems = () => {
  //   const { stateObject } = this.state;
  //   const newItems = this.state.todoList.filter(
  //     item => item.completed === viewCompleted
  //   );
  //   return newItems.map(item => (
  //     <li 
  //       key={item.id}
  //       className="list-group-item d-flex justify-content-between align-items-center"
  //     >
  //       <span 
  //         className={`todo-title mr-2 ${
  //           this.state.viewCompleted ? "completed-todo" : ""
  //         }`}
  //         title={item.description}
  //         >
  //           {item.title}
  //         </span>
  //     </li>
  //   ));
  // };

  render() {
    return (
      <main className="container">
        <h1 className="text-black text-uppercase text-center my-4">The Store</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                >
                  add a thing
                </button>
              </div>
              {/* {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul> */}
            </div>
          </div>
        </div>
      </main>
    );
  }
}
export default App;
