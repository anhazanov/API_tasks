// class FreeDomain extends React.Component {
//    render(){
//     return (
//         <h1>WE ARE THE CHAMPIONS!</h1>
//         )
//     }
// }

// ReactDOM.render(<FreeDomain/>, document.getElementById("ukraine_free_domains"))


class UkraineFreeDomains extends React.Component {
    state = { details: []}
  
    handClick = () => {
      let data;
      axios.get("/tasks/api/free_domains/")
      .then(res => {
        data = res.data;
        this.setState({ details: data})
      })
      .catch( err => {
        console.log(err)
      })
    }
  
    // componentDidMount() {
    //   let data;
    //   axios.get("/tasks/api/free_domains/")
    //   .then(res => {
    //     data = res.data;
    //     this.setState({ details: data})
    //   })
    //   .catch( err => {
    //     console.log(err)
    //   })
    // }
  
    render() {
      return (
        <div class="white_shd full margin_bottom_30">
          <div class="full graph_head">
              <div class="heading1 margin_0">
                <h2>Список освобожденных доменов</h2>
              </div>
          </div>
          <div class="full graph_head">
            <button type="button" class="btn cur-p btn-info" onClick={this.handClick}>Полуть список освобожденных доменов</button>
          </div>
          <div class="table_section padding_infor_info">
              <div class="table-responsive-sm">
                <table class="table">
                    <thead>
                      <tr>
                          <th>Домен</th>
                          <th>ID в системе</th>
                          <th>Дата освобождения</th>
                          <th>Trust</th>
                      </tr>
                    </thead>
                    <tbody>
                    {this.state.details.map((output, id) => (
                      <tr key={id}>
                        <td>{output.name}</td>
                        <td>{output.id}</td>
                        <td>{output.expired_dtime}</td>
                        <td>{output.trust}</td>
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
  
  ReactDOM.render(<UkraineFreeDomains/>, document.getElementById("ukraine_free_domains"))