open System

let n = int(Console.In.ReadLine())
let poly = Console.In.ReadLine().Split " "
let arithmetic (x,y,z)=
    match (x,y,z) with
    | (x,y,0) -> (x+y)
    | (x,y,_) -> z*(x+y)

for i in 1..n do
    printfn "%A" (arithmetic (int (poly.[0]),(int poly.[1]),i)) 
