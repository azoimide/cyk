% names = { 'td_gen_grammar1.txt.csv', 'bu_gen_grammar1.txt.csv', 'naive_gen_grammar1.txt.csv' }
% names = { 'td_rand_grammar1.txt.csv', 'bu_rand_grammar1.txt.csv', 'naive_rand_grammar1.txt.csv' }
% names = { 'td_gen_grammar2.txt.csv', 'bu_gen_grammar2.txt.csv', 'naive_gen_grammar2.txt.csv' }
% names = { 'td_rand_grammar2.txt.csv', 'bu_rand_grammar2.txt.csv', 'naive_rand_grammar2.txt.csv' }
% names = { 'td_gen_grammar3.txt.csv', 'bu_gen_grammar3.txt.csv', 'naive_gen_grammar3.txt.csv' }
% names = { 'td_rand_grammar3.txt.csv', 'bu_rand_grammar3.txt.csv', 'naive_rand_grammar3.txt.csv' }
% names = { 'td_rand_grammar4.txt.csv', 'bu_rand_grammar4.txt.csv', 'naive_rand_grammar4.txt.csv' }
% names = { 'td_gen_grammar4.txt.csv', 'bu_gen_grammar4.txt.csv', 'naive_gen_grammar4.txt.csv' }

all_names = {...
    { 'td_gen_grammar1.txt.csv', 'bu_gen_grammar1.txt.csv', 'naive_gen_grammar1.txt.csv' },...
    { 'td_rand_grammar1.txt.csv', 'bu_rand_grammar1.txt.csv', 'naive_rand_grammar1.txt.csv' },...
    { 'td_gen_grammar2.txt.csv', 'bu_gen_grammar2.txt.csv', 'naive_gen_grammar2.txt.csv' },...
    { 'td_rand_grammar2.txt.csv', 'bu_rand_grammar2.txt.csv', 'naive_rand_grammar2.txt.csv' },...
    { 'td_gen_grammar3.txt.csv', 'bu_gen_grammar3.txt.csv', 'naive_gen_grammar3.txt.csv' },...
    { 'td_rand_grammar3.txt.csv', 'bu_rand_grammar3.txt.csv', 'naive_rand_grammar3.txt.csv' },...
    { 'td_rand_grammar4.txt.csv', 'bu_rand_grammar4.txt.csv', 'naive_rand_grammar4.txt.csv' },...
    { 'td_gen_grammar4.txt.csv', 'bu_gen_grammar4.txt.csv', 'naive_gen_grammar4.txt.csv' }};

grammars = {...
    'Matching brackets',...
    'Right-linear scientific notation',...
    'Equal ''a''s and ''b''s',...
    'Left-linear scientific notation'};

modes = {'random strings', 'strings in language'};
modes_short = {'rand', 'gen'};

for i=1:length(all_names)

    names = all_names{i};
    d1 = csvread(names{1});
    d2 = csvread(names{2});
    d3 = csvread(names{3});

    if i == 1
        fprintf('\\\\\n\\textbf{Grammar %d} & \\textbf{Top down} & \\textbf{Bottom up} & \\textbf{Naive} \\\\\n\\hline\n', ceil(i / 2));
    elseif mod(i, 2) == 1
        fprintf('\\\\\n\\textbf{Grammar %d} \\\\\n\\hline\n', ceil(i / 2));
    end
    fprintf('\\textbf{%-20s}', modes{mod(i, 2) + 1});
    for j=1:length(names)
        data = csvread(names{j});
        x = data(:,1);
        y = data(:,2);
        cs = polyfit(log(x), log(y), 1);
        fprintf(' & %f', cs(1));
    end
    fprintf(' \\\\\n');
   
%     figure('Visible', 'off');
%     plot(d1(:, 1), d1(:, 2), d2(:, 1), d2(:, 2), d3(:, 1), d3(:, 2));
%     legend('Top down', 'Bottom up', 'Naive');
%     xlabel('String length');
%     ylabel('Time (s)');
%     title(strcat(grammars{ceil(i / 2)}, {' - '}, modes{mod(i, 2) + 1}));
%     
%     % legend(names);
%     
%     % plot(d1(:, 1), d1(:, 2), d3(:, 1), d3(:, 2));
%     % legend(names{1}, names{3});
%     
%     % plot(d1(:, 1), d1(:, 2), d2(:, 1), d2(:, 2));
%     % legend(names(1:2));
%     fname = strcat('g', num2str(ceil(i / 2)), '_', modes_short{mod(i, 2) + 1}, '.png');
%     saveas(gcf, fname);
    % pause
end
