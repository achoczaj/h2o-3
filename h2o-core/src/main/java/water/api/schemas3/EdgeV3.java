package water.api.schemas3;

import water.api.API;
import hex.mli.Edge;

public class EdgeV3 extends RequestSchemaV3<Edge,EdgeV3> {
    @API(help="Node a", direction = API.Direction.OUTPUT)
    public int node_a;

    @API(help="nodeb", direction = API.Direction.OUTPUT)
    public int node_b;

    @API(help="weight", direction = API.Direction.OUTPUT)
    public double weight;

}
