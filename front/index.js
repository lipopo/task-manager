import React from 'react';
import ReactDOM from 'react-dom';

import App from './app.jsx';


let app_container = document.querySelector("#app");


ReactDOM.render(
    React.createElement(App), app_container
);
