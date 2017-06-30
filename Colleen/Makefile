# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tettouat <tettouat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/05/20 16:49:38 by tettouat          #+#    #+#              #
#    Updated: 2016/05/20 16:50:01 by tettouat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = Colleen

CFLAG = -Wall -Werror -Wextra

SRCC = Colleen.c

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

re: fclean all

.PHONY: all clean fclean re