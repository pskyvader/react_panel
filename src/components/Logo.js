import React, { Component } from 'react';
class Logo extends Component {
  constructor(props) {
    super(props);
  }
  componentDidMount() {
    fetch(API)
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }
}
export default Logo;