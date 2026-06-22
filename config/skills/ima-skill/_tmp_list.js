const { execSync } = require("child_process");
const cmd = 'node ima_api.cjs openapi/wiki/v1/get_knowledge_list \'{"knowledge_base_id":"9P9LfmFJRFwLidUrzKQu0cZZ5QMVxtv61QA9iFoV90g=","cursor":"","limit":50}\'';
try {
  const resp = JSON.parse(execSync(cmd, { cwd: __dirname }));
  console.log(JSON.stringify(resp, null, 2));
} catch(e) {
  console.error("STDERR:", e.stderr?.toString());
  console.error("STDOUT:", e.stdout?.toString());
}
