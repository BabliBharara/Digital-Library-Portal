let availablesearch=[
    'Btech(cse)','BCA','B.Pharma','BBA','JK',
];
const resultbox= document.querySelector(".resultbox");
const input1=document.getElementById("input");
input1.onkeyup=function()
{
    let result = [];
    let inputs = input1.value;
    if(inputs.length){
        result=availablesearch.filter((keyword)=>{
           return keyword.toLowerCase().includes(inputs.toLowerCase());
        });
        console.log(result);
    }
    display(result);

    if(!result.length){
        resultbox.innerHTML ='';
    }
}
function display(result){
    const content = result.map((list)=>{
        return "<li onclick=selectInput(this)>" + list + "</li>";
 });
     resultbox.innerHTML = "<ul>" + content.join('') + "</ul>";
}
function selectInput(list){
    input1.value = list.innerHTML;
    resultbox.innerHTML ='';
}
    

