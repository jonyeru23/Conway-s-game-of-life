window.addEventListener("load", ()=>{
    const canvas = document.querySelector("#canvas");
    const cxt = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    console.log("it worked");
});