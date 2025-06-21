/**
 * Plotly graph resize functionality for Solar Path Visualizer
 * Ensures graphs resize properly on window resize and page load
 */

// Force Plotly graphs to resize when window is resized
window.addEventListener('resize', function() {
    // Trigger resize event for all Plotly graphs
    if (window.Plotly) {
        const graphs = document.querySelectorAll('.js-plotly-plot');
        graphs.forEach(function(graph) {
            if (graph && graph._fullLayout) {
                Plotly.Plots.resize(graph);
            }
        });
    }
});

// Also resize graphs after a short delay when page loads
window.addEventListener('load', function() {
    setTimeout(function() {
        if (window.Plotly) {
            const graphs = document.querySelectorAll('.js-plotly-plot');
            graphs.forEach(function(graph) {
                if (graph && graph._fullLayout) {
                    Plotly.Plots.resize(graph);
                }
            });
        }
    }, 100);
}); 