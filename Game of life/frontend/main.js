window.addEventListener("load", ()=>{
    const canvas = document.querySelector("#canvas");
    const cxt = canvas.getContext("2d");

    resizeCanvas();

    setGrid(cxt, canvas);
    setTheGame(canvas)
    console.log("it worked");
});

window.addEventListener("resize", resizeCanvas());

function resizeCanvas(){
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

function setGrid(cxt, canvas){
    for (let i = 0; i < canvas.width; i+=15){
        cxt.beginPath();
        cxt.moveTo(i, 0);
        cxt.lineTo(i, canvas.height);
        cxt.strokeStyle = 'wheat';
        cxt.stroke();
    }
    for (let j = 0; j < canvas.height; j+=15){
        cxt.beginPath();
        cxt.moveTo(0, j);
        cxt.lineTo(canvas.width, j);
        cxt.strokeStyle = 'wheat';
        cxt.stroke();
    }
}

function setTheGame(canvas){
    let population = []
    for (let i = 0; i < canvas.width; i += 15){
        let populationLine = []
        for (let j = 0; j < canvas.width; j += 15){
            if (Math.random() <= 0.4){
                populationLine.push(true);
            }
            else {populationLine.push(false);}
        }
        population.push(populationLine)
    }
    console.log(population);
}

// function draw(population){
//     for (let i = 0; i < canvas.width; i += 15){
//         for (let j = 0; j < canvas.width; j += 15){
//             if 
//         }
//     }
// }