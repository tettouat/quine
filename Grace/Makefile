# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tettouat <tettouat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/05/20 16:55:23 by tettouat          #+#    #+#              #
#    Updated: 2016/05/20 16:56:02 by tettouat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = Grace

CFLAG = -Wall -Werror -Wextra

SRCC = Grace.c

SRCO = $(SRCC:.c=.o)

all: $(NAME)

$(NAME): $(SRCO)
	clang $(SRCO) -o $(NAME)

%.o: %.c
	clang $(FLAGS) -c $< -o $@

clean:
	rm -f $(SRCO)

fclean: clean
	rm -f $(NAME)
	rm -f Grace_kid.c

re: fclean all

.PHONY: all clean fclean re