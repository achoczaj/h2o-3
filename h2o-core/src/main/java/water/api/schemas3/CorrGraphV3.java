package water.api.schemas3;

import hex.mli.CorrGraph;
import water.api.API;
import water.api.schemas3.KeyV3.FrameKeyV3;

public class CorrGraphV3 extends RequestSchemaV3<CorrGraph,CorrGraphV3> {
    @API(help="input correlation frame id", direction = API.Direction.INPUT)
    public FrameKeyV3 cor_frame_id;

    @API(help="column indexes to filter `corrFrame` by", direction = API.Direction.INPUT)
    public int[] col_idxs;

    @API(help="threshold", direction = API.Direction.INPUT)
    public double threshold;

    @API(help="edges", direction = API.Direction.OUTPUT)
    public EdgeV3[] edges;

    @API(help="edges", direction = API.Direction.OUTPUT)
    public String[] nodes;

}
