
from ariadne import gql

type_defs = gql("""
    input CozmoSpeakInput {
        id: ID!
        sentence: String!
    }

    input RandomAnimationInput {
        id: ID!
    }

     type Query {
        cozmoSpeak(input: CozmoSpeakInput): String,
        random_animation(input:RandomAnimationInput): [String]
    }

    
""")
