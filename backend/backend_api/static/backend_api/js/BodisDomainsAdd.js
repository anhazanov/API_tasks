class DomainInput extends React.Component {
    render() {
        return(<input />)
    }
}

class BodisDomainsAdd extends React.Component {
    constructor (props) {
        super(props);
        this.state = {
            domains_fields: 1,
            domains_list: [],
            message: ""
        };
        this.handleInput = this.handleInput.bind(this);
        this.divList = this.divList.bind(this);
        this.changeInput = this.changeInput.bind(this);
    }

    handleInput = () => {
        let value = this.state.domains_fields + 1
        this.setState({domains_fields: this.state.domains_fields + 1})
    }

    changeInput = (event, i) => {
        let temp = this.state.domains_list

        if (temp.at(i) || temp.at(i) !== ' ') {temp[i] = event.target.value}
        else {temp.push(event.target.value)}

        this.setState ({domains_list: temp})
    }

    divList() {
        const rowList = [];
        for (let i = 0; i < this.state.domains_fields; i++) {
          rowList.push(<div className="crud-card" id="input_domain"><input onChange={(event) => this.changeInput(event, i)}/></div>);
        }
        return rowList;
      }
    
    addDomains = () => {
        let data;
        const domains_list = this.state.domains_list
        axios.post("/tasks/api/add_domains_bodis", domains_list)
        .then (res => {
            data = res.data;
            if (data) {
                this.setState ({
                    domains_fields: 0,
                    domain_list: [],
                    message: "Домены добавлены"
                })
                this.handleInput()
            }
            else {
                this.setState ({
                    message: "Произошла ошибка"
                })
            }
        });
    }

    render() {
        return (
            <div class="white_shd full margin_bottom_30">
                <div class="full graph_head">
                    <div>
                    <h3>Добавить список домены</h3><br/>
                    </div>
                    <div>
                    {this.divList()}
                    </div>
                    { this.state.message 
                        ? <div>{this.state.message}</div>
                        : null
                    }
                    <button class="btn cur-p btn-success" onClick={this.handleInput}>Ввести еще домен</button>  
                    <button class="btn cur-p btn-danger" type="button" onClick={this.addDomains}>Добавить домены</button>
                </div>
            </div>
        )
    }
}

ReactDOM.render(<BodisDomainsAdd/>, document.getElementById("bodis_domains"))