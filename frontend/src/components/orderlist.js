import { Link } from "react-router-dom";
import { useLocation } from "react-router-dom";


function OrderList(props) {
    const location = useLocation();
    console.log(location, "gotcha");
    const data = location.state?.data;
    console.log(data, "the data I need");

    let total = 0;

    for (let key in data) {
        total += data[key][2];
    }

    return (
        <div className="container mt-4 ">
            <div className="card text-center">
                <div className="card-header">
                    Review Order
                </div>
                <div className="card-body">
                    <h5 className="card-title">Special title treatment</h5>
                    <p className="card-text">With supporting text below as a natural lead-in to additional content.</p>
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Item_Pic</th>
                                <th scope="col">Items</th>
                                <th scope="col">Price</th>
                                <th scope="col">Quantity</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Object.entries(data).map(([key, [name, quantity, price]]) => (
                                <tr key={key}>
                                    <th scope="row">1</th>
                                    <td>Pic</td>
                                    <td>{name}</td>
                                    <td>{price}</td>
                                    <td>{quantity}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
                <div className="card-footer text-muted">
                    <p>Grand Total: {total} </p>
                    <Link to="/payment_method" className="btn btn-primary">Payment</Link>
                </div>
            </div>
        </div>
    );
};

export default OrderList;