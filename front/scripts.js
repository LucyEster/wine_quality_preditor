/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/vinhos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => 
      response.json()
    )
    .then((data) => {
      console.log(data)
      data.vinhos.forEach(item => insertList(
        item.fixed_acidity,
        item.volatile_acidity, 
        item.citric_acid,
        item.residual_sugar,
        item.chlorides,
        item.free_sulfur_dioxide,
        item.total_sulfur_dioxide,
        item.density,
        item.p_h,
        item.sulphates,
        item.alcohol,
        item.quality
        ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()



/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (fixed_acidity, volatile_acidity, citric_acid,
  residual_sugar, chlorides, free_sulfur_dioxide,
  total_sulfur_dioxide, density, p_h, sulphates, alcohol) => {
    
  const formData = new FormData();
  formData.append('fixed_acidity', fixed_acidity);
  formData.append('volatile_acidity', volatile_acidity);
  formData.append('citric_acid', citric_acid);
  formData.append('residual_sugar', residual_sugar);
  formData.append('chlorides', chlorides);
  formData.append('free_sulfur_dioxide', free_sulfur_dioxide);
  formData.append('total_sulfur_dioxide', total_sulfur_dioxide);
  formData.append('density', density);
  formData.append('p_h', p_h);
  formData.append('sulphates', sulphates);
  formData.append('alcohol', alcohol);

  let url = 'http://127.0.0.1:5000/vinho';
  
  return new Promise((resolve, reject) => {
    fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => resolve(data))
    .catch((error) => {
      console.error('Error:', error);
    });
  });
}


/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  
  let fixed_acidity = document.getElementById("fixed_acidity").value;
  let volatile_acidity = document.getElementById("volatile_acidity").value;
  let citric_acid = document.getElementById("citric_acid").value;
  let residual_sugar = document.getElementById("residual_sugar").value;
  let chlorides = document.getElementById("chlorides").value;
  let free_sulfur_dioxide = document.getElementById("free_sulfur_dioxide").value;
  let total_sulfur_dioxide = document.getElementById("total_sulfur_dioxide").value;
  let density = document.getElementById("density").value;
  let p_h = document.getElementById("p_h").value;
  let sulphates = document.getElementById("sulphates").value;
  let alcohol = document.getElementById("alcohol").value;

  
  postItem(fixed_acidity, volatile_acidity, citric_acid,
    residual_sugar, chlorides, free_sulfur_dioxide,
    total_sulfur_dioxide, density, p_h, sulphates, alcohol)
  .then((data) => {
    insertList(fixed_acidity, volatile_acidity, citric_acid,
      residual_sugar, chlorides, free_sulfur_dioxide,
      total_sulfur_dioxide, density, p_h, sulphates, alcohol, data.quality);
  });
      

}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
  chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, p_h, sulphates,
  alcohol, quality) => {

  var item = [fixed_acidity,
              volatile_acidity, 
              citric_acid, 
              residual_sugar, 
              chlorides, 
              free_sulfur_dioxide, 
              total_sulfur_dioxide, 
              density, 
              p_h, 
              sulphates,
              alcohol,
              quality];

  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  document.getElementById("fixed_acidity").value = "";
  document.getElementById("volatile_acidity").value = "";
  document.getElementById("citric_acid").value = "";
  document.getElementById("residual_sugar").value = "";
  document.getElementById("chlorides").value = "";
  document.getElementById("free_sulfur_dioxide").value = "";
  document.getElementById("total_sulfur_dioxide").value = "";
  document.getElementById("density").value = "";
  document.getElementById("p_h").value = "";
  document.getElementById("sulphates").value = "";
  document.getElementById("alcohol").value = "";

}