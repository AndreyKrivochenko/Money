import React from "react";

const CounterpartyItem = ({counterparty}) => {
    return (
        <tr>
            <td>{counterparty.id}</td>
            <td>{counterparty.name}</td>
            <td>{counterparty.description}</td>
        </tr>
    )
}

const CounterpatiesList = ({counterpaties}) => {
    return (
        <table className="table">
            <thead>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
        </thead>
        <tbody>
            {counterpaties.map((c) => <CounterpartyItem counterparty={c} />)}
        </tbody>
        </table>
    )
}

export default CounterpatiesList