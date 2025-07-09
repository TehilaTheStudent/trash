import axios from 'axios';

async function run() {
    const url = '';
    // const url = 'https://remote-mcp-server-authless-2.hrwnwbyzt.workers.dev/sse';

    try {
        const response = await axios.get(url, {
            headers: {
                'Accept': 'text/event-stream'
            },
            timeout: 10000 // prevent hanging forever
        });

        console.log(`✅ Response received with status: ${response.status}`);
        console.log('Response body:\n', response.data);
    } catch (err) {
        console.error('❌ Request failed:', err.message);
    }
}

run();
