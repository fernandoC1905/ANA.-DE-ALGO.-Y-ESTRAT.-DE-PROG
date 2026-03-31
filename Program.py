edad : int = 18
altura : float = 1.80
nom : str = "Carlos"
ape = 'Chan'
esVerde : bool = True
mayorEdad = True

print(f"{nom} {ape} tiene {edad} años y su carro {"es" if esVerde else "no es"} verde")

print(f"su altura es {altura} metros")

print(f"{nom} {ape} {"es" if mayorEdad else "no es"} mayor de edad")