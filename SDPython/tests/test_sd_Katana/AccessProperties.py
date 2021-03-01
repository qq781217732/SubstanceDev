import sd
# Import the required classes.
from sd.api.sdproperty import SDPropertyCategory
from sd.api.sdvalueserializer import SDValueSerializer

# Get and print information regarding the selected nodes.
def printSelectedNodesInfo(nodes):
    for node in nodes:
        definition = node.getDefinition()
        nodeId = node.getIdentifier()

        print("node %s, id = %s" % (definition.getLabel(), nodeId))

        # Create a list of each property category enumeration item.
        categories = [
            SDPropertyCategory.Annotation,
            SDPropertyCategory.Input,
            SDPropertyCategory.Output
        ]

        # Get node properties for each property category.
        for category in categories:
            props = definition.getProperties(category)

            # Get the label and identifier of each property.
            for prop in props:
                label = prop.getLabel()
                propId = prop.getId()

                # Get the connection for the currently accessed property.
                if prop.isConnectable():
                    connections = node.getPropertyConnections(prop)

                    if connections:
                        print("Propery %s is connected!!!" % label)
                        continue

                # Get the value for the currently accessed property.
                value = node.getPropertyValue(prop)

                if value:
                    print("Property %s, id = %s, value = %s" % (label, propId, SDValueSerializer.sToString(value)))