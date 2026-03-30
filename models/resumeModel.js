const mongoose = require("mongoose");

const resumeSchema = new mongoose.Schema({

skills:[String],

jobRole:String,

score:Number,

suggestions:[String]

});

module.exports = mongoose.model("Resume",resumeSchema);