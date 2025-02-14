import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import React from 'react'
import { Routes, Route } from "react-router-dom"
import { ToastContainer} from "react-toastify"
import Home from './d_compo/Home.js';
function App() {


  return (
    <>
      {/* <Header /> */}
      <Routes>
       
        {/* register components */}
        <Route path='/' element={<Home />} />
       



      </Routes>
      <ToastContainer position="top-center" />
    </>
  );
}

export default App;
