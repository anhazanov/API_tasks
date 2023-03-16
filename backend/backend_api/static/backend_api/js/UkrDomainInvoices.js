class UkraineDomainInvoices extends React.Component {
    state = {invoices_list: []}

    handClick = () => {
        let data;
        axios.get("/tasks/api/get_invoices/")
        .then(res => {
            data = res.data;
            console.log(data);
            this.setState({ invoices_list: data})
        })
        .catch( err => {
            console.log(err)
        })
    }

    cancelInvoice = (id) => {
        let data = {"id": id}
        axios.post("/tasks/api/cancel_invoices/", data)
        .catch( err => { console.log(err) })
        this.handClick()
    }

    componentDidMount() {
        let data;
        axios.get("/tasks/api/get_invoices/")
        .then(res => {
            data = res.data;
            console.log(data);
            this.setState({ invoices_list: data})
        })
        .catch( err => {
            console.log(err)
        })
    }

    payBalance = (id) => {
        let data = {"id": id};
        axios.post("/tasks/api/pay_invoice_balance/", data)
        .catch( err => { console.log(err) })
        this.handClick()
    }

    render () {
        return (
            <div class="white_shd full margin_bottom_30">
                <div class="full graph_head">
                    <div class="heading1 margin_0">
                    <h2>Список счетов для оплаты доменов</h2>
                    </div>
                </div>
                <div class="full graph_head">
                <button type="button" class="btn cur-p btn-info" onClick={this.handClick}>Обновить список созданных счетов для регистрации доменов</button>
                </div>
                <div class="table_section padding_infor_info">
                    <div class="table-responsive-sm">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Описание</th>
                                <th>ID в системе</th>
                                <th>Статус</th>
                                <th>Отменить заявку</th>
                                <th>Оплатить</th>
                            </tr>
                        </thead>
                        <tbody>
                        {this.state.invoices_list.map((output, id) => (
                            <tr key={id}>
                            <td>{output.purpose}</td>
                            <td>{output.id}</td>
                            <td>{output.status}</td>
                            <td><button class="btn cur-p btn-danger" onClick={() => this.cancelInvoice(output.id)}>Отменить заявку</button></td>
                            <td>
                                <a class="dropdown-toggle" data-toggle="dropdown"><button class="btn cur-p btn-danger">Оплатить</button></a>
                                <div class="dropdown-menu">
                                    <a class="dropdown-item" href="#" onClick={() => this.payBalance(output.id)}>С баланса пользователя</a>
                                    <a class="dropdown-item" href="#">Через Приват24</a>
                                </div>
                            </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                    </div>
                </div>
            </div>
            )   
        }
    }

ReactDOM.render(<UkraineDomainInvoices/>, document.getElementById("ukraine_domain_invoices"))