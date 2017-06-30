# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tettouat <tettouat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/05/20 15:02:51 by tettouat          #+#    #+#              #
#    Updated: 2016/05/20 16:51:20 by tettouat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = Sully

CFLAG = -Wall -Werror -Wextra

SRCC = Sully.c

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
	rm -f Sully_*
re: fclean all

.PHONY: all clean fclean re