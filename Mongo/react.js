import React from 'react';
// import {toast} from 'react-toastify';
// import 'react-toastify/dist/ReactToastify.css';

//toast.configure();
export default class App extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      _id:'',
      name:'',
      preci:'',
      books:[]//Array par recoger los recursos de books
    };
  }

  refreshBooks(){
    const apiUrl = `http://localhost:5600/books`;
    fetch(apiUrl)
    .then((response) => response.json())
    .then((data) =>{
        this.setState({books:data});
        console.log(this.state.books);
    })
  }

  //Metodo que se ejecuta al cargar este componente
  componentDidMount(){
    this.refreshBooks();
  }

  render(){
    return (
      <div className="container">
        <h1 style={{color:'green'}}>Biblioteca</h1>

      </div>
    );
  }
}