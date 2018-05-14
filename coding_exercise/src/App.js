import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      request_failed: false,
      data: null
    }
  }

  componentDidMount() {
    fetch('http://localhost:8000/differences')
      .then(response => {
        if (!response.ok) {
          throw Error("Network request failed")
        }

        return response
      })
      .then(d => d.json())
      .then(d => { this.setState({data: d}); }, () => { this.setState({request_failed: true}); })
  }
  render() {
    if (this.state.request_failed) return <p>Failed!</p>
    if (this.state.data === null) return <p>Loading...</p>
    if (this.state.data === []) return <p>There have been no requests</p>
    return (
      <div>

        <h2>Here are the past requests</h2>
        <table>
          <thead>
            <th>number</th>
            <th>value</th>
            <th>datetime</th>
            <th>last datetime</th>
            <th>occurences</th>
          </thead>
          <tbody>
            {this.state.data.map((d) => (
              <tr>
                <td>{d.number}</td>
                <td>{d.value}</td>
                <td>{d.datetime}</td>
                <td>{d.last_datetime}</td>
                <td>{d.occurrences}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default App;
