class UkraineDomainRegistration extends React.Component {
    constructor (props) {
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
        axios.defaults.xsrfCookieName = "csrftoken";
        super(props);
        this.state = {check_domain: "", ch_domain: "", domain: "", period: "", pay_data: ""};
        this.sendPostCheckDomain = this.sendPostCheckDomain.bind(this);
        this.sendPostRegistrDomain = this.sendPostRegistrDomain.bind(this);
        this.handleChangeCheck = this.handleChangeCheck.bind(this);
        this.handleChangeDomain = this.handleChangeDomain.bind(this);
        this.handleChangePeriod = this.handleChangePeriod.bind(this);

    }

    handleChangeCheck = event => {
        this.setState ({
            ch_domain: event.target.value
        })
      }

    handleChangeDomain = event => {
        this.setState ({
            domain: event.target.value
        })
      }
    
    handleChangePeriod = event => {
        this.setState ({
            period: event.target.value
        })
    }

    sendPostCheckDomain = () => {
        let data;
        const ch_domain = this.state.ch_domain;
        axios.post("/tasks/api/check_domain/", {ch_domain})
        .then(res => {
            data = res.data;
            this.setState ({ check_domain: data })
            })
        .catch( err => {
            console.log(err)
            })
        }

    sendPostRegistrDomain = () => {
        let data_registr;
        const registr = this.state
        axios.post("/tasks/api/registr_domain/", {registr})
        .then(res => {
        data_registr = res.data;
        this.setState ({ pay_data: data_registr });
    })
    .catch( err => {
      console.log(err)
    })
    }

    payContent = (pay_domain, pay_price) => {
        return (
            <div class="table-responsive-sm">
              <table class="table">
                  <thead>
                    <tr>
                        <th>Домен</th>
                        <th>Сумма к оплате</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>{pay_domain}</td>
                      <td>{pay_price}</td>
                    </tr>
                  </tbody>
              </table>
            </div>
        )
    }

    render() {
        let content;
        let ch_domain = this.state.ch_domain;
        if (this.state.check_domain === "Домен свободен") {
            content = <p>Домен {ch_domain} свободен</p>
        }
        else if (this.state.check_domain === "Домен занят")
        { content = <p>Домен {ch_domain} занят</p> }

        let pay_content;
        if (this.state.pay_data.price) {
            pay_content = this.payContent (this.state.pay_data.domain, this.state.pay_data.price)
        }

        else if (! this.state.pay_data) {pay_content = ''}

        else if (! this.state.pay_data.price && this.state.pay_data &&this.state.pay_data.domain ) {
            pay_content = this.payContent (this.state.pay_data.domain, "Домен не доступен")
        }
        

        return (
        <div> 
            <div class="white_shd full margin_bottom_30">
                <div class="full graph_head">
                    <div class="heading1 margin_0">
                    <h2>Проверка доступности домена</h2>
                    </div>
                </div>
                <div class="full graph_head">
                    <input placeholder="Введите домен" name="domain" type="text" onChange={this.handleChangeCheck}/><br />
                    <button type="sumbit" class="btn cur-p btn-info" onClick={this.sendPostCheckDomain}>Проверить доступность домена</button><br />
                    {content}
                </div>
            </div>

            <div class="white_shd full margin_bottom_30">
                <div class="full graph_head">
                    <div class="heading1 margin_0">
                    <h2>Создание счета для оплаты регистрации домена</h2>
                    </div>
                </div>
                <div class="full graph_head">
                    <input placeholder="Введите домен" name="domain" type="text" onChange={this.handleChangeDomain}/><br />
                    <input placeholder="Срок регистрации, лет" name="period" type="text" onChange={this.handleChangePeriod}/><br />
                    <button type="sumbit" class="btn cur-p btn-info" onClick={this.sendPostRegistrDomain}>Создать заказ на регистрацию</button><br />
                    <div class="table_section padding_infor_info">
                        {pay_content}
                    </div>
                </div>
            </div>
            
        </div>
        )
    }
}

ReactDOM.render(<UkraineDomainRegistration/>, document.getElementById("ukraine_domain_registration"))