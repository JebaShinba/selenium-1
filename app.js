const { MongoClient } = require('mongodb');

// Connection URL
const url = 'mongodb://localhost:27017';
const client = new MongoClient(url);

async function run() {
    try {
        // Connect to the MongoDB server
        await client.connect();
        console.log("Connected to MongoDB");

        // Create a new database
        const db = client.db('my_database');  // Replace 'my_database' with your desired database name

        // Create a new collection
        const collection = db.collection('my_collection');  // Replace 'my_collection' with your desired collection name

        // Insert documents
        const document = { name: "John Doe", age: 30, city: "New York" };
        await collection.insertOne(document);
        
        const documents = [
            { name: "Alice", age: 25, city: "Los Angeles" },
            { name: "Bob", age: 28, city: "Chicago" }
        ];
        await collection.insertMany(documents);
        console.log("Documents inserted successfully.");

        // Query the database
        const foundDoc = await collection.findOne({ name: "John Doe" });
        console.log("Found document:", foundDoc);

        const allDocs = await collection.find().toArray();
        console.log("All documents:", allDocs);
        
    } catch (err) {
        console.error("Error connecting to MongoDB:", err);
    } finally {
        // Close the connection
        await client.close();
    }
}

// Run the function
run().catch(console.dir);
