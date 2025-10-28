let availablesearch=[
    'Btech(cse)','bca','B.pharma','bba',
];
const resultbox= document.querySelector(".resultbox");
const input=document.getElementById("input");
input.onkeyup=function()
{
    let result=[];
    let input1=input.value;
    if(input1.length){
        result=availablesearch.filter((keyword)=>{
           return keyword.toLowerCase().includes(input1.toLowerCase());
        });
        console.log(result);
    }
    display(result);
}
function display(result){
    const content=result.map((list)=>{
        return "<li>"+ list + "</li>"
 });
 resultbox.innerHTML="<ul>"+ content.join('') +"</ul>";
}
    

