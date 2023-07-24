
/*
* Vars & Const
*/
//const budget_form = document.getElementById('budget_form');
const budget_submit = document.getElementById('budget_submit');
//const budget_amount = document.getElementById('budget_amount');

/*
* Event Listeners
*/

budget_submit.addEventListener('click', function(e){
    e.preventDefault();
    const budget_amount = document.getElementById('budget_amount');
    const budget_periodic = document.querySelector('input[name="budget_periodic"]:checked');
    const postData = new FormData();
    postData.append('budget_amount',budget_amount.value)
    postData.append('budget_periodic',budget_periodic.value)
    
    initial_budget_info(postData);
})

/*
* Functions
*/

function initial_budget_info(postData=null){
    const budget_form = document.getElementById('budget_form');
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const request = new Request(
        budget_form.action,
        {
            method: 'post',
            body: postData,
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin',
            
        }
    );

    fetch(request).then(r => r.json()).then(data => set_budget_info(data));
    
    return;
}

initial_budget_info();

function set_budget_info(data){
    const annual_budget_div = document.getElementById("annual_budget_div")
    const monthly_budget_div = document.getElementById("monthly_budget_div")
    const weekly_budget_div = document.getElementById("weekly_budget_div")

    annual_budget_div.innerHTML = formatMoney(data[0].fields.annual)
    monthly_budget_div.innerHTML = formatMoney(data[0].fields.month)
    weekly_budget_div.innerHTML = formatMoney(data[0].fields.week)

    return;
}

function formatMoney(amount, decimalCount = 2, decimal = ".", thousands = ",") {
    try {
      decimalCount = Math.abs(decimalCount);
      decimalCount = isNaN(decimalCount) ? 2 : decimalCount;
  
      const negativeSign = amount < 0 ? "-$" : "$";
  
      let i = parseInt(amount = Math.abs(Number(amount) || 0).toFixed(decimalCount)).toString();
      let j = (i.length > 3) ? i.length % 3 : 0;
  
      return negativeSign + 
        (j ? i.substr(0, j) + thousands : '') +
        i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thousands) +
        (decimalCount ? decimal + Math.abs(amount - i).toFixed(decimalCount).slice(2) : "");
    } catch (e) {
      console.log(e)
    }
  };