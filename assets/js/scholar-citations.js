(function () {
    'use strict';
    var config = window.scholarCitationConfig || {};
    var current = null;
    var status = document.getElementById('citation-status');

    function timestamp(data) {
        // New snapshots carry an explicit UTC offset. Legacy timestamps were UTC on Actions.
        var value = data && data.updated;
        if (typeof value !== 'string') return NaN;
        if (!/[zZ]$|[+-]\d\d:\d\d$/.test(value)) value = value.replace(' ', 'T') + 'Z';
        return Date.parse(value);
    }

    function render(data) {
        var time = timestamp(data);
        if (!data || data.scholar_id !== 'ORwuKSYAAAAJ' || !data.publications ||
            !Object.keys(data.publications).length || !Number.isFinite(time)) return false;
        if (current && time < timestamp(current)) return false;
        current = data;
        var total = document.getElementById('total_cit');
        if (total && Number.isInteger(data.citedby) && data.citedby >= 0) total.textContent = data.citedby;
        Array.prototype.forEach.call(document.querySelectorAll('.show_paper_citations'), function (element) {
            var publication = data.publications[element.getAttribute('data')];
            var count = publication && publication.num_citations;
            element.textContent = '引用：' + (Number.isInteger(count) && count >= 0 ? count : '暂无数据');
        });
        if (status) {
            var label = data.collection_method === 'automated' ? '最近成功抓取' : '最近核实快照';
            status.textContent = 'Google Scholar 引用 · 每日尝试更新（UTC 08:00），非实时同步。' + label + '：' + new Date(time).toISOString().replace('T', ' ').replace('.000Z', ' UTC') + '。';
            if (Date.now() - time > 48 * 60 * 60 * 1000) status.textContent += ' 数据已超过48小时未更新。';
        }
        return true;
    }

    function unavailable() {
        if (status) status.textContent += current ? ' 未取得更新数据，保留上次可用快照。' : ' 引用数据暂不可用。';
    }

    render(config.snapshot);
    if (!config.url) { unavailable(); return; }
    var controller = new AbortController();
    var timeout = setTimeout(function () { controller.abort(); }, 10000);
    fetch(config.url, { signal: controller.signal, cache: 'no-cache' })
        .then(function (response) {
            if (!response.ok) throw new Error('Citation request failed');
            return response.json();
        })
        .then(function (data) {
            if (!render(data)) unavailable();
        })
        .catch(unavailable)
        .finally(function () { clearTimeout(timeout); });
}());
