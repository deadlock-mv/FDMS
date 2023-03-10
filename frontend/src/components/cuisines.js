import { render } from "react-dom";
import { useParams } from "react-router-dom";
// import { getcuisine } from "./services/services";
import {Link} from 'react-router-dom';
import { useState, useEffect } from "react";
import axios from "axios";

function Cuisines() {
    // let id = { useParams };
    const [data, setData] = useState({});
    const [total, setTotal] = useState();
    const [cuisine, setCuisine] = useState([]);
    const loginstatus = localStorage.getItem('loginstatus');
    // using for getting data from api 
    useEffect(() => {
        getCuisine()
    }, []);

    // using for calculating total after each update 
    useEffect(() => {
        let amt = 0;
    
        for (let key in data) {
            amt += data[key][2];
            if (data[key][2]==0){
                let deldata = data;
                delete deldata[key];
                setData(deldata);
            }
        }
    
        setTotal(amt);
    }, [data]);

    // getting data from api 
    function getCuisine() {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/Category/",
        }).then((response) => {
            const data = response.data
            setCuisine(data)
        }).catch((error) => {
            if (error.response) {
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);

            }
        })
    }

    // updating dataset named 'data' with objects of type [id: quantity, value] pair after each click 
    let handleInput = (event, itemlist) => {
        let amt = 0;
        const key = itemlist.id;
        const name = itemlist.itemname;
        const quantity = Number(event.target.value);
        const val = (itemlist.price) * quantity;
        setData(prevData => {
            const updatedData = { ...prevData, [key]: [name, quantity, val] };
            Object.entries(updatedData).forEach(([key, value]) => console.log(`${key}: ${value}`));
            return updatedData;
        });
    }


    // sidebar Styling
    const sidebar = {
        height: "200px",
        width: "600px",
        position: "fixed",
        top: 80,
        left: 0,
        paddingtop: "40px",
        backgroundcolor: "lightblue",
        margin: "20px"
    };
    return (

        <div className="container mt-4">
            <div className="row">

                {/* sidebar def */}
                <div style={sidebar} >
                    <aside className="col-md-4 col-sm-3">
                        <div className="card">
                            <h5 className="card-header">Menu</h5>
                            <div id="list-example" className="list-group list-group-flush">
                               
                                {/* Menu tab for loop populating */}
                                {cuisine.map((menu) => (
                                    <a className="list-group-item list-group-item-action" href={"#list-item-" + menu.id}>{menu.categoryname}</a>
                                ))}
                               
                            </div>
                        </div>
                    </aside>
                </div>
                {/* sidebar def end */}

                {/* main body items  */}
                <section className="col-md-8 col-sm-6 ms-4 p-5">
                    <div className="card p-5" >
                        <div data-spy="scroll" data-target="#list-example" data-offset="0" className="scrollspy-example">
                            
                            {/* populating order list table */}
                            {cuisine.map((menu, idx) => (
                                <>
                                    <h4 id={"list-item-" + menu.id}>{menu.categoryname}</h4>
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
                                        {menu.items.map((itemlist) => (
                                            <tbody>
                                                <tr>
                                                    <th scope="row">1</th>
                                                    <td>Pic</td>
                                                    <td>{itemlist.itemname}</td>
                                                    <td>{itemlist.price}</td>
                                                    <td><input type="number" min='0' max='5' id={itemlist} name={itemlist.id}
                                                        onChange={(e) => handleInput(e, itemlist)}  required />
                                                    </td>
                                                </tr>
                                            </tbody>
                                        ))}
                                    </table>
                                </>
                            ))}
                        {/* populating order list table end */}

                        </div>
                    </div>
                </section>
                {/* main body items end  */}

                {/* Total Card -- total is counted on each update  */}
                <div>
                    <div className="card" style={{ width: "20rem" }}>
                        <div className="card-header">
                            <h5>Total Amount</h5>
                        </div>
                        {loginstatus=='true' &&
                        <div className="card-body">
                            <h5 className="card-title">{total}</h5>
                            <Link to="/order_review" state={{data: data}} className="btn btn-primary">Place Order</Link>
                        </div>
                        }
                        {loginstatus!='true' &&
                        <div className="card-body">
                            <h5 className="card-title">{total}</h5>
                            <Link to="/login"  className="btn btn-primary">Login to Order</Link>
                        </div>
                        }
                    </div>
                </div>
            </div>
        </div>

    );
}

export default Cuisines;