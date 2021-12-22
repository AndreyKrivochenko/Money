import React from "react";
import axios from "axios";
import CounterpatiesList from "./components/counterpaties";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'counterpaties': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/counterparties/')
            .then(response => {
                const counterpaties = response.data;
                this.setState({
                    'counterpaties': counterpaties
                    })
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <CounterpatiesList counterpaties={this.state.counterpaties} />
            </div>
        )
    }
}

export default App;
