import React, { Component } from "react";

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount(){
    // For initial data
    this.fetchData();
  }

  fetchData = () => {
    fetch("http://127.0.0.1:8000/api/color_swatch/v1/color_palette/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
        const renderColorCode =(color_type:string, color)=>{
      if(color_type === 'rgb'){
        return (
            <span className="color-info" key={color.id}>
              RGB <p style={{margin:"5px"}}>({color.red},{color.green},{color.blue})</p>
          </span>
        )
      }
      if(color_type === 'hsl'){
         return (
            <span className="color-info" key={color.id}>
              HSL <p style={{margin:"5px"}}>({color.hue},{color.saturation},{color.lightness}) </p>
            </span>
         )
      }
      if(color_type === 'brgb'){
        return (
            <span className="color-info" key={color.id}>
              BRGB <p style={{margin:"5px"}}> ({color.red},{color.green},{color.blue}) </p>
            </span>
        )
      }
    }

    return (
      <div>
        <div className="color-list">
            <div className="color-palette">
                <h2></h2>
                <div className="color-container width5 clearfix">
                  <h3>Color Swatch</h3>
                  {this.state.data.map(color =>
                    <span className="color tooltiptext" key={color.id} style={{background:color.hex_color}}>
                        {renderColorCode(color.color_type, color)}
                    </span>
                  )}
                </div>
                <div className="cell">
                    <button type="submit" className="circle" value="" onClick={this.fetchData}></button>
                    <div className="info-text">Generate New Swatch</div>
                </div>
            </div>
        </div>
      </div>
    );
  }

}

export default App;
