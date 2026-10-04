const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('assets/js/scholar-citations.js', 'utf8');
const snapshot = JSON.parse(fs.readFileSync('_data/scholar_snapshot.json', 'utf8'));
async function run(remote) {
    const status = { textContent: '' };
    const elements = Object.keys(snapshot.publications).map(id => ({getAttribute: () => id, textContent: ''}));
    const context = {
        window: {scholarCitationConfig: {snapshot, url: 'fixture'}},
        document: {getElementById: id => id === 'citation-status' ? status : null, querySelectorAll: () => elements},
        AbortController, setTimeout, clearTimeout,
        fetch: () => remote instanceof Error ? Promise.reject(remote) : Promise.resolve({ok: true, json: () => Promise.resolve(remote)})
    };
    vm.runInNewContext(source, context);
    await new Promise(resolve => setImmediate(resolve));
    return {elements, status};
}
(async () => {
    let view = await run(new Error('Offline'));
    assert.equal(view.elements[0].textContent, '引用：84');
    assert.equal(view.elements.filter(e => e.textContent === '引用：暂无数据').length, 2);
    assert.match(view.status.textContent, /保留上次可用快照/);
    view = await run({...snapshot, updated: '2026-09-07T00:00:00Z', publications: {}});
    assert.equal(view.elements[0].textContent, '引用：84');
    view = await run({...snapshot, updated: '2026-10-05T00:00:00Z', collection_method: 'automated', publications: {'ORwuKSYAAAAJ:unknown': {num_citations: 1}}});
    assert.ok(view.elements.every(e => e.textContent === '引用：暂无数据'));
    assert.match(view.status.textContent, /最近成功抓取/);
    console.log('Frontend tests passed: no total_cit element, offline fallback, stale data, missing counts.');
})();
