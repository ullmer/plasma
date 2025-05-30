
import py4j.GatewayServer;
import io.microraft.RaftNode;
import io.microraft.RaftNodeBuilder;
import io.microraft.model.RaftModelFactory;
import io.microraft.model.impl.DefaultRaftModelFactory;

public class RaftNodeApp {

    private RaftNode raftNode;

    public RaftNodeApp() {
        RaftModelFactory modelFactory = new DefaultRaftModelFactory();
        this.raftNode = RaftNodeBuilder.newBuilder()
            .setGroupId("my-raft-group")
            .setLocalEndpoint(() -> "node-1")
            .setModelFactory(modelFactory)
            .build();
    }

    public String getStatus() {
        return raftNode.getStatus().name();
    }

    public static void main(String[] args) {
        RaftNodeApp app = new RaftNodeApp();
        GatewayServer server = new GatewayServer(app);
        server.start();
        System.out.println("Py4J Gateway Server started.");
    }
}
