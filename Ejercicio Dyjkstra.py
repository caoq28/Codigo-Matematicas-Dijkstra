import heapq

def dijkstra(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    anteriores = {nodo: None for nodo in grafo}

    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia, nodo = heapq.heappop(cola)

        if nodo == destino:
            break

        for vecino, peso in grafo[nodo].items():
            nueva_distancia = distancia + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo
                heapq.heappush(
                    cola, (nueva_distancia, vecino)
                )

    return distancias[destino]
