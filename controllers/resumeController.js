const { exec } = require("child_process");
const Resume = require("../models/resumeModel");

exports.analyzeResume = async (req,res)=>{

const filePath = req.file.path;

exec(`python ../ai_module/resume_parser.py ${filePath}`, async (error, stdout)=>{

if(error){
return res.status(500).json({error:"Python processing error"});
}

const result = JSON.parse(stdout);

const newResume = new Resume({
skills: result.skills,
score: result.score,
suggestions: result.suggestions,
jobRole: result.job_role
});

await newResume.save();

res.json(result);

});

};