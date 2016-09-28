% names = { 'td_gen_grammar1.txt.csv', 'bu_gen_grammar1.txt.csv', 'naive_gen_grammar1.txt.csv' }
% names = { 'td_rand_grammar1.txt.csv', 'bu_rand_grammar1.txt.csv', 'naive_rand_grammar1.txt.csv' }
% names = { 'td_gen_grammar2.txt.csv', 'bu_gen_grammar2.txt.csv', 'naive_gen_grammar2.txt.csv' }
% names = { 'td_rand_grammar2.txt.csv', 'bu_rand_grammar2.txt.csv', 'naive_rand_grammar2.txt.csv' }
% names = { 'td_gen_grammar3.txt.csv', 'bu_gen_grammar3.txt.csv', 'naive_gen_grammar3.txt.csv' }
names = { 'td_rand_grammar3.txt.csv', 'bu_rand_grammar3.txt.csv', 'naive_rand_grammar3.txt.csv' }

d1 = csvread(names{1});
d2 = csvread(names{2});
d3 = csvread(names{3});

% plot(d1(:, 1), d1(:, 2), d2(:, 1), d2(:, 2), d3(:, 1), d3(:, 2));
% legend(names);

% plot(d1(:, 1), d1(:, 2), d3(:, 1), d3(:, 2));
% legend(names{1}, names{3});

plot(d1(:, 1), d1(:, 2), d2(:, 1), d2(:, 2));
legend(names(1:2));
