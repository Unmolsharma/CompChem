class square
{
    sideLength;
    cornerX;
    cornerY;


    constructor (cornerX, cornerY, sideLength)
    {
        this.cornerX = cornerX;
        this.cornerY = cornerY;
        this.sideLength = sideLength;
    
    }

    draw(d)
    {
        d.beginPath();
        d.rect(this.cornerX, this.cornerY, this.sideLength, this.sideLength);
        d.fillStyle = colour;
        d.fill();
        
    }
}

function go()
{
    for (i=0; i< 10; i++)
    {
        setTimeout(drawSquare,i*3000);
    }   
}
function drawSquare()
{
    xC = parseInt(document.getElementById("xValue").value);
    yC = parseInt(document.getElementById("yValue").value);
    sideLength = parseInt(document.getElementById("side").value);
    colour = document.getElementById("colour").value;

    sq = new square(xC, yC, sideLength);
    ctx = document.getElementById("drawArea").getContext("2d");
    sq.draw(ctx);

    i = 0
    while (i < 10) {

        sq = new square (xC, yC, sideLength);
        ctx = document.getElementById("drawArea").getContext("2d");

        sq.draw(ctx);
        xC += 10
        yC += 10
        i += 1;
    }
}